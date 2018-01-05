import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

import { AppData } from '../../back/app-data';
import { Message } from '../../back/app-data';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  private appData: AppData = new AppData();
  private messages: Message[];

  constructor(public navCtrl: NavController) {

  }

  ionViewWillEnter() {
  //   this.appData.getEntries().then((entries) => {
  //     this.messages = entries;
  //   });
  //   console.log("GOT ENTRIES for MESSSAGES in HOME PAGE");
  //   console.log(this.messages);
  this.appData.getEntries().then((entries) => {
    this.messages = entries;
  });
  console.log("GOT entry method called");
  console.log(this.messages);
  }

}
