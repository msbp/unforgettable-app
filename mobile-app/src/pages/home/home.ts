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
  private getUrl: string = 'https://unforgettable.herokuapp.com/getMessages';
  private deleteByIdUrl: String = 'https://unforgettable.herokuapp.com/deleteMessageById';

  private messages: Message[];
  // There will be an array for title and body. This array will
  // carry the title and body to be displayed on the application.
  // cardInformation[].title and cardInformation[].body .
  private cardInformation = [];

  constructor(public navCtrl: NavController, private transport: Transport) {

  }

  sampleId(str: string){
    console.log('ID IS: ' + str);
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
      this.messages = data;
      return data;
    }, (error) => {
      console.log('Error ocurred calling getRequest.\nError: ' + error);
      return error;
    });
  }

  // This method creates arrays with text from Message object
  // The view will automatically update the elements based on this array
  createArraysFromObject(){
    this.cardInformation = [];
    for (let message of this.messages){
      let t = message.day + ' - ' + message.hour + ':' + message.minute;
      this.cardInformation.push({title:t, body:message.body, id:message.id});
    }
  }

  // This method is used to delete a Message from the database.
  // It should reload the main page once it has run.
  deleteMessageById(id: string){
    this.transport.getRequest(this.deleteByIdUrl + '?id=' + id).then((data: string) => {
      console.log('deleteMessageById called, status returned: ' + data);
    }, (error) => {
      console.log('Error ocurred calling deleteMessageById.\nError: ' + error);
    });
  }
  
}
