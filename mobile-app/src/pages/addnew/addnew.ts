import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { AlertController } from 'ionic-angular';

import { Message } from '../../models/message.service';
import { Transport } from '../../models/transport';

/**
 * Generated class for the AddnewPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-addnew',
  templateUrl: 'addnew.html',
  providers: [Transport]
})
export class AddnewPage {
  private static postUrl: string = 'https://unforgettable.herokuapp.com/addMessage';

  private message: Message = {
    day: '',
    hour: 0,
    minute: 0,
    time: '12:30',
    body: ''
  };

  constructor(public navCtrl: NavController, public navParams: NavParams, private transport: Transport, private alertController:AlertController) {
    console.log('Constructor called.');
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad AddnewPage');
  }

  addMessage() {
    if (this.checkInput() === false){
      this.showAlert('Invalid Input', 'Please make sure your input is valid. Try again.');
      return;
    }
    this.postRequest();
    // AddnewPage.gotId = false;
    this.showAlert('Status', 'Your message has been sent to the server.');
    this.navCtrl.pop();
  }

  // This method uses the Transport class to post the data of a Message object
  // to a server specified in the postUrl variable
  postRequest() {
    this.translateTime();
    let body = {
      day: this.message.day,
      hour: this.message.hour,
      minute: this.message.minute,
      time: this.message.time,
      body: this.message.body
    };
    this.transport.postRequest(AddnewPage.postUrl, body).then((data) => {
    console.log('Status:\n' + data);
    return data;
    }, (error) => {
      console.log('Error occurred:\n' + error);
      return error;
    });
  }

  // This method checks the input fields to see if they have been filled
  // out properly. Returns true or false
  checkInput(): boolean{
    if (this.message.day === '' || this.message.body === ''){
      return false;
    }
    return true;
  }

  // This method reads the string that carries the time and translates it into
  // hour and minute number variables
  translateTime() {
    let time: string = this.message.time;
    let arr: string[] = time.split(':');
    this.message.hour = Number(arr[0]);
    this.message.minute = Number(arr[1]);
  }

  // This method presents title of header and message of data
  showAlert(header: string, data: string){
    let alert = this.alertController.create({
      title: header,
      message: data,
      buttons: [{text:'Ok',
                role: 'cancel',
                handler: () =>{
                  console.log('Ok pressed.');
                }}]
    });
    alert.present();
  }

}
