import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { Message } from '../../models/message.service';
import { Transport } from '../../models/transport.ts';

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

  message: Message = {
    day: '',
    hour: 0,
    minute: 0,
    time: '12:30',
    body: ''
  };

  constructor(public navCtrl: NavController, public navParams: NavParams, private transport: Transport) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad AddnewPage');
  }

  addMessage() {
    this.samplePost();
  }

  samplePost(){
    let body = {
      day: this.message.day,
      hour: this.message.hour,
      minute: this.message.minute,
      time: this.message.time,
      body: this.message.body
    };

    this.transport.postRequest('https://unforgettable.herokuapp.com/sample', body).then((data) => {
      console.log('here is the post: '+ data);
    },
      (error) => {
        console.log('Error occurs: ' + error);
      });
  }





}
