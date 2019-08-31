import { Component, OnInit, OnDestroy } from '@angular/core';
import { Tweet } from '../models/tweet.model';
import { TweetService } from '../services/tweet.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-twitter-result',
  templateUrl: './twitter-result.component.html',
  styleUrls: ['./twitter-result.component.css']
})
export class TwitterResultComponent implements OnInit, OnDestroy {
  tweets: Tweet[];
  outputRatingAsText = ['Extreme Negative', 'Negative', 'Neutral', 'Postive', 'Extreme Postive']
  subscription: Subscription;
  
  constructor(
    private tweetService: TweetService
  ) { }

  ngOnInit() {
    this.subscription = this.tweetService.tweetsChanged.subscribe(
      tweets => this.tweets = tweets
    )
  }

  ngOnDestroy(){
    this.subscription.unsubscribe();
  }

}
