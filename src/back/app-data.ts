import { Storage } from '@ionic/storage';

export class AppData {
  private storage: Storage;
  private message: Message;
  private entries: Message[];

  // entries variable is an array that keeps track of Message objects
  constructor(){
    //Initializing variables
    this.storage = new Storage({name:'my_database'});
    this.entries = [];
  }

  // Method adds a Message entry to the array of messages
  // This method should work with the server to add messages
  addEntry(day:string, hour:number, minute:number, msg:string) {
    this.message = new Message(day, hour, minute, msg);
    this.entries.push(this.message);
    this.storage.set('entries', this.entries);
    console.log("Adding it to:");
    console.log(this.storage);
  }

  // Method retrieves the array of messages
  // This method should work with the server to get messages ---
  getEntries(): Message[]{
    return this.storage.get('entries').then((entries) => {
      this.entries = entries == null ? [] : entries;
      return this.entries;
    });
  }

}

// Class used to hold message values
class Message {
  private day: string;
  private hour: number;
  private minute: number;
  private msg: string;

  constructor(day:string, hour:number, minute:number, msg:string){
    this.day = day;
    this.hour = hour;
    this.minute = minute;
    this.msg = msg;
  }
}
