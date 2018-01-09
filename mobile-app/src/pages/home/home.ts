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
  private message: Message;

  constructor(public navCtrl: NavController, private transport: Transport) {

  }

  // This method uses the Transport class to retrieve a list of the data of Message
  // objects from the specified server in the getUrl variable.
  // It should only be called if there was a change in the list
  getRequest() {
    this.transport.getRequest(this.getUrl).then((data) => {
      console.log('Get Request:\n' + data);
      return data;
    }, (error) => {
      console.log('Error ocurred:\n' + error);
      return error;
    });
  }

  // This method is used to add each specific message to the view
  addMessageToView (){

  }

}
