import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Tweet } from '../models/tweet.model';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class GetTweetsService {

  baseUrl = environment.baseUrl;

  constructor(private httpClient: HttpClient) { }

  getweets(searchKeyword: string, count: number){
    const url = this.baseUrl + 'twitter/' + searchKeyword + '/' + count;
    return this.httpClient.get<Tweet[]>(url).pipe(
      map(tweets => tweets.map(tweetJson => {
        if(!tweetJson[0].retweeted_status) {
          return new Tweet(
            tweetJson[0].full_text,
            tweetJson[0].user.name,
            tweetJson[0].user.screen_name,
            tweetJson[0].user.profile_image_url_https,
          tweetJson[1]);
        }else{
          return new Tweet(
            tweetJson[0].retweeted_status.full_text,
            tweetJson[0].retweeted_status.user.name,
            tweetJson[0].retweeted_status.user.screen_name,
            tweetJson[0].retweeted_status.user.profile_image_url_https,
          tweetJson[1]);
        }
      }))
    );
  }
}
