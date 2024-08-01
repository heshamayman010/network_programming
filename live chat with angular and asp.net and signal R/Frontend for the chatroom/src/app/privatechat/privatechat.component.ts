import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { ChatserviceService } from '../../services/chatservice.service';

@Component({
  selector: 'app-privatechat',
  templateUrl: './privatechat.component.html',
  styleUrl: './privatechat.component.css'
})
export class PrivatechatComponent implements OnInit,OnDestroy {

// here we will take the input from the user as we will work on it using the moddal 

@Input() touser:string='';

constructor(public activemodal:NgbActiveModal,public myservice:ChatserviceService) {
  
}
  ngOnDestroy(): void {
  
  // in the destroy we will only close the private chat 

  this.myservice.closeprivatechat(this.touser);
  }
  ngOnInit(): void {
  
  }

// this function is only for the private chat 
sendmessage(content:string){

this.myservice.sendprivatemessage(this.touser,content)

}

}
