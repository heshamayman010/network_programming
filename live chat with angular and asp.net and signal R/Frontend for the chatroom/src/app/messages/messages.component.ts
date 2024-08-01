import { Component, Input } from '@angular/core';
import { Messages } from '../models/messages';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrl: './messages.component.css'
})
export class MessagesComponent {
// this component is mainly used to recieve and handle the messages from the users

@Input() mymessages:Messages[] =[];


}
