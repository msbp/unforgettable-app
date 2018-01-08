import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class Transport {

  constructor(private http: Http){

  }

  postRequest(url:string, data){
    let body = data;
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    let options = new RequestOptions({
      headers: headers
    });

    return new Promise((resolve, reject) => {
      this.http.post(url, body, options).toPromise().then(response => {
        resolve(response['_body'])
      }).catch(error => {
        reject(error)
      })
    })
  }

}
