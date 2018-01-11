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

  private postUrl: string = 'http://127.0.0.1:8000/addMessage';

  private message: Message = {
    day: '',
    hour: 0,
    minute: 0,
    time: '12:30',
    body: ''
  };

  constructor(public navCtrl: NavController, public navParams: NavParams, private transport: Transport, private alertController:AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad AddnewPage');
  }

  addMessage() {
    this.postRequest();
    this.showAlert('Status', 'Your message has been sent to the server.');
  }

  // This method uses the Transport class to post the data of a Message object
  // to a server specified in the postUrl variable
  postRequest() {
    let body = {
      day: this.message.day,
      hour: this.message.hour,
      minute: this.message.minute,
      time: this.message.time,
      body: this.message.body
    };

    this.transport.postRequest(this.postUrl, body).then((data) => {
    console.log('Status:\n' + data);
    return data;
    }, (error) => {
      console.log('Error occurred:\n' + error);
      return error;
    });
  }

  // This method presents title of header and message of data
  showAlert(header: string, data: string){
    let alert = this.alertController.create({
      title: header,
      message: data,
      buttons: [{text:'Ok',
                role: 'cancel',
                handler: () =>{
                  console.log('Cancel pressed. Leaving screen.');
                  this.navCtrl.pop();
                }}]
    });
    alert.present();
  }

}
