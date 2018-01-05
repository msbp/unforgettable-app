import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { Message } from '../../models/message.service';

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
})
export class AddnewPage {

  message: Message = {
    day: '',
    hour: 0,
    minute: 0,
    time: '12:30',
    body: ''
  };

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad AddnewPage');
  }

  addMessage() {
    console.log('Message to be added:');
    console.log(this.message);
  }

}
