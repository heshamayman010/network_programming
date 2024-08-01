import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { text } from 'stream/consumers';
import { User } from '../app/models/user';
import { HubConnection, HubConnectionBuilder } from '@microsoft/signalr';
import { error } from 'console';
import { Messages } from '../app/models/messages';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { PrivatechatComponent } from '../app/privatechat/privatechat.component';

@Injectable({
  providedIn: 'root'
})
export class ChatserviceService {

  // then we clarify the hub variable 

  private chatconnection?:HubConnection;
  myname :string='';
  liveusers:string[]=[]
  messages:Messages []=[];  // the messages that will be recieved 

  privatemessages:Messages[]=[]  // this will be ussed to store the private messages only
  privatemessageintiated:boolean=false; 

  apiurl="http://localhost:15832/api/chat/RegisterUser";
  
  connectionurl="http://localhost:15832/hubs/chat"
  constructor(private http:HttpClient,public modalservice:NgbModal ) {


   }


   // this will only be used to register the users into the chat room 
    registerUser(user :User){
// here we must add the return in the method as it returns observable
return this.http.post(this.apiurl,user,{responseType:'text'})
      
    }


// function to create the connection and process every event from the server to handle the incomming messages and events
createchatconnection() {
  this.chatconnection = new HubConnectionBuilder().withUrl(this.connectionurl).withAutomaticReconnect().build();

  // Start the connection
  this.chatconnection.start().catch(error => {
    console.error(error);
  });

  // userconnected this funtion is the function from the api that will be trigared after the connection id is add at the OnConnectedAsync
this.chatconnection.on('userconnected',()=>{
this.adduserconnectionid()});

this.chatconnection.on('liveusers',(liveusers)=>{
  // we will save the users we got from the server in our array 
this.liveusers=[...liveusers]

})



this.chatconnection.on("Newmessage",(thenewmessage:Messages)=>{
// here we will create new message array with the old messages and the new message 
  this.messages=[...this.messages,thenewmessage]

})

// the next part is for the private users chat 
//----------------------------------------------------------

//1-
this.chatconnection.on('openprivatechat',(newmessage:Messages)=>{
// here after the open we will store the messages in the array 
  this.privatemessages=[...this.privatemessages,newmessage]
this.privatemessageintiated=true;
// the next part is for the modal 

// and the next one is for the modal dialog to open it using the chat component inside it 
const modalref=this.modalservice.open(PrivatechatComponent);
// the componentInstance is used in the modal to give you access to the instances inside the componanet that will open 
modalref.componentInstance.touser=newmessage.from;
})


//2-

this.chatconnection.on('newprivatemessage',(newmessage:Messages)=>{
  // we will save the users we got from the server in our array 
this.privatemessages=[...this.privatemessages,newmessage]

})

//3- for closing the private chat 

this.chatconnection.on('closeprivatechat',()=>{
  // we will save the users we got from the server in our array 
this.privatemessages=[];
this.privatemessageintiated=false;
// then close the modal dialog
this.modalservice.dismissAll();

})


}

// Method to stop the connection
stopconnection() {
  this.chatconnection?.stop().catch(error => {
    console.error(error);
  });
}


async adduserconnectionid(){
// here it is used to invoke the name of the server method to call or the api method to call 
   return this.chatconnection?.invoke('Adduserconnectionid',this.myname).catch(error=>console.log(error));
}


// function to send the messages  here we will use the interface of themessage and then invoke the function 
//in the server to recieve it with the message data from and also the content of it 

async sendmessage(content :string){

const messagtosend:Messages={

  from:this.myname,
  content
}



return this.chatconnection?.invoke("RecieveMessage",messagtosend).catch(error=>{
  console.log(error)
})
}

// the next part is for the private chat all functionlaities 
//--------------------------------------------------------------

 async closeprivatechat(touser:string){

  return this.chatconnection?.invoke("RemovePrivateChat",touser,this.myname).catch(error=>{
  console.log(error)
})}



// this function will mainly be used to send  and create private chat then send it to the private   
async sendprivatemessage(touser:string, content:string){
// here we will send the message as usual put 

const privatemessagtosend:Messages={

  from:this.myname,
  // check for this 
  to:touser
  ,content
}
// here we will make the check to sea if the private message is sent from us or it is recieved from the another user
if(!this.privatemessageintiated){
this.privatemessageintiated=true;

  return this.chatconnection?.invoke("CreatePrivateChat",privatemessagtosend)
  // then we will use call back function to store the messages in the private messages array 
  .then(()=>
  {
    this.privatemessages=[...this.privatemessages,privatemessagtosend]
  })
  .catch(error=>{
  console.log(error)

})

}else{
  // here if it is not sent message so we will recieve one 
  return this.chatconnection?.invoke("RecievePrivateMessage",privatemessagtosend).catch(error=>{
  console.log(error)

  
})

}}}
