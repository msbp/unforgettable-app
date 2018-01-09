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

  private transport: Transport;
  private postUrl: string = 'http://127.0.0.1:8000/sample';
  private postStatus: string = 'Not Sent';

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
    this.showAlert();
  }

  // This method uses the Transport class to post the data of a Message object
  // to a server specified in the urlPost variable
  postRequest(){
    let body = {
      day: this.message.day,
      hour: this.message.hour,
      minute: this.message.minute,
      time: this.message.time,
      body: this.message.body
    };

      this.transport.postRequest(this.postUrl, body).then((data) => {
      console.log('Status: ' + data);
      return data;
    }, (error) => {
      console.log('Error occurred:\n' + error);
      return error;
    });

  }

  showAlert(data: string){
    let alert = this.alertController.create({
      title: 'Status:',
      message: 'You message has been sent to the server.',
      buttons: [{text:'Cancel',
                role: 'cancel',
                handler: () =>{
                  console.log('Cancel pressed. Leaving screen.');
                  this.navCtrl.pop();
                }}]
    });
    alert.present();
  }

}
