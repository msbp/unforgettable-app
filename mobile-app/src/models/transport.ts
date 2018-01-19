import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';
import { Message } from './message.service';

@Injectable()
export class Transport {

  constructor(private http: Http){

  }

  // This method is used to make post requests to a server
  postRequest(url: string, data) {
    let body = data;
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    let options = new RequestOptions({
      headers: headers
    });

    return new Promise((resolve, reject) => {
      this.http.post(url, body, options).toPromise().then(response => {
        resolve(response) //Return response['_body'] to get json
      }).catch(error => {
        reject(error)
      })
    })
  }

  // This method is used to make get requests to a server
  getRequest(url: string) {
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    let options = new RequestOptions({
      headers: headers
    });

    return new Promise((resolve, reject) => {
      this.http.get(url, options).toPromise().then(response => {
        console.log('Response from GET request:' + response['_body']);
        resolve(response.json());
      }).catch(error => {
        reject(error)
      });
    });
  }

}
