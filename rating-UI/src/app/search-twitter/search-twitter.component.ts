import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { TweetService } from '../services/tweet.service';

@Component({
  selector: 'app-search-twitter',
  templateUrl: './search-twitter.component.html',
  styleUrls: ['./search-twitter.component.css']
})
export class SearchTwitterComponent implements OnInit {

  getTweetsForm = new FormGroup({
    searchKeyword: new FormControl('', Validators.required),
    count: new FormControl('', Validators.required)
  })

  constructor(
    private tweetService: TweetService
    ) { }

  ngOnInit() {
  }

  onSubmit(){
    this.tweetService.getTweetsBySearchKeywordAndCount(
      this.getTweetsForm.get('searchKeyword').value,
      this.getTweetsForm.get('count').value);
  }
}
