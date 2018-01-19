import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Message } from '../../models/message.service';
import { Transport } from '../../models/transport';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html',
  providers: [Transport]
})

export class HomePage {
  private getUrl: string = 'http://127.0.0.1:8000/getMessages';

  private messages: Message[];
  // There will be arrays for title and body. These arrays will
  // carry the title and body to be displayed on the application.
  // title[0] corresponds to body[0] and so on.
  private title: string[];
  private body: string[];

  constructor(public navCtrl: NavController, private transport: Transport) {

  }

  ionViewWillEnter(){
    this.messages = this.getRequest();
    
  }

  // This method uses the Transport class to retrieve a list of the data of Message
  // objects from the specified server in the getUrl variable.
  // It should only be called if there was a change in the list
  getRequest() : Message[]{
    return this.transport.getRequest(this.getUrl).then((data: Message[]) => {
      console.log('Get Request:\n' + data);
      console.log('Sample:' + data[4].body)
      return data;
    }, (error) => {
      console.log('Error ocurred:\n' + error);
      return error;
    });
  }

  // This method is used to add each specific message to the view
  addMessageToView (data: dictionary[]){

  }

}
