import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { AppData } from '../../back/app-data';
import { Message } from '../../back/app-data';

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
  private appData: AppData = new AppData();
  private messages: Message[];

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad AddnewPage');
  }

  addEntry(): void {
    this.appData.addEntry('Today', 13, 30, 'This is my message body.');
    console.log("Add entry method called");
  }

  getEntry(): void{
    this.appData.getEntries().then((entries) => {
      this.messages = entries;
    });
    console.log("Get entry method called")
    console.log(this.messages)
  }

}
