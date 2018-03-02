import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { AlertController } from 'ionic-angular';
import { LoadingController } from 'ionic-angular';

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

  constructor(public navCtrl: NavController, private transport: Transport, private alertController: AlertController, private loadingController: LoadingController) {

  }

  // This method is automatically called when the view is about to enter
  ionViewWillEnter(){
    this.updateViewWithMessages();
  }

  // This method is responsible for the refresher component of the page
  doRefresh(refresher){
    refresher.pullMin = 110;
    refresher.pullMax = refresher.pullMin + 200;
    this.updateViewWithMessages();
    console.log('Refresher has been called.');
    setTimeout(() => {
      console.log('Operation has ended.');
      refresher.complete();
    }/*, 1000*/);
}

  // This method is used to update the messages on the view.
  // It returns false if messages is undefined. Otherwise it returns true.
  updateViewWithMessages(){
    this.getRequest();
    if (this.messages == undefined){
      return false;
    }
    this.createArraysFromObject();
    return true;
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
      //this.showAlert('Status', 'An error occurred deleting the item.');
      console.log('Error ocurred calling deleteMessageById.\nError: ' + error);
    });
    this.showAlert('Status', 'Your message has successfully been deleted.');
    this.updateViewWithMessages();
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

  // This method displays a loading controller
  // The parameter passed is the time in ms
  presentLoadingController(t: number){
    let loading = this.loadingController.create({
      spinner: 'crescent',
      content: 'Loading please wait'
    });
    loading.present();
    setTimeout(() => {
      loading.dismiss();
    }, t);
  }

}
