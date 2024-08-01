import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { HomeComponent } from './home/home.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, provideHttpClient } from '@angular/common/http';
import { ChatComponent } from './chat/chat.component';
import { ChatinputComponent } from './chatinput/chatinput.component';
import { MessagesComponent } from './messages/messages.component';
import { PrivatechatComponent } from './privatechat/privatechat.component';
import { UserhomeComponent } from './userhome/userhome.component';
import { UserchatComponent } from './userchat/userchat.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    HomeComponent,
    ChatComponent,
    ChatinputComponent,
    MessagesComponent,
    PrivatechatComponent,
    UserhomeComponent,
    UserchatComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,ReactiveFormsModule,
    HttpClientModule,FormsModule
  ],
  providers: [
    provideClientHydration(),
    provideHttpClient()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
