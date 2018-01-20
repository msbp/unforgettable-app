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
  // There will be an array for title and body. This array will
  // carry the title and body to be displayed on the application.
  // cardInformation[].title and cardInformation[].body .
  private cardInformation = [];

  constructor(public navCtrl: NavController, private transport: Transport) {

  }

  ionViewWillEnter(){
    this.getRequest();
    //Change this code to be in the get request code. so it occurs in order.
    if (this.messages == undefined){
      return
    }
    this.createArraysFromObject();
  }

  // This method uses the Transport class to retrieve a list of the data of Message
  // objects from the specified server in the getUrl variable.
  // It should only be called if there was a change in the list
  getRequest(){
      this.transport.getRequest(this.getUrl).then((data: Message[]) => {
      console.log('Get Request:\n' + data);
      console.log('Sample:' + data[4].body)
      this.messages = data;
      return data;
    }, (error) => {
      console.log('Error ocurred:\n' + error);
      return error;
    });
  }

  // This method creates arrays with text from Message object
  // The view will automatically update the elements based on this array
  createArraysFromObject(){
    this.cardInformation = [];
    for (let message of this.messages){
      let t = message.day + ' - ' + message.hour + ':' + message.minute;
      this.cardInformation.push({title:t, body:message.body});
    }
  }

}
