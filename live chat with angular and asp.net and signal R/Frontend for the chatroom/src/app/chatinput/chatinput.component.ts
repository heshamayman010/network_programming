import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-chatinput',
  templateUrl: './chatinput.component.html',
  styleUrl: './chatinput.component.css'
})
export class ChatinputComponent {

messagecontent:string='';

// here we will emit the message from the child componeent to the parent component so we will use output 

@Output() contentemitter=new EventEmitter();
sendmessage(){
  // first we must check if the message is empty or not 
if(this.messagecontent.trim()!==""){
this.contentemitter.emit(this.messagecontent)
}
// then we must make the content empty again 
this.messagecontent='';
}
}
