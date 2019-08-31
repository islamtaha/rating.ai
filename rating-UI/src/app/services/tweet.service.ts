import { Injectable } from '@angular/core';
import { Tweet } from '../models/tweet.model';
import { GetTweetsService } from './get-tweets.service';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TweetService {
  tweets: Tweet[] = [];
  tweetsChanged: Subject<Tweet[]> = new Subject<Tweet[]>();
  constructor(
    private getTweetsService: GetTweetsService
    ) { }
  
  getTweetsBySearchKeywordAndCount(searchKeyword: string, count: number){
    this.getTweetsService.getweets(searchKeyword, count).subscribe(
      tweets => {
        this.tweets = tweets;
        this.tweetsChanged.next(this.tweets);
      }
    );
  }
}
