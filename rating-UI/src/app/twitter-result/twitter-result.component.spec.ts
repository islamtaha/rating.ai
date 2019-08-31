import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TwitterResultComponent } from './twitter-result.component';

describe('TwitterResultComponent', () => {
  let component: TwitterResultComponent;
  let fixture: ComponentFixture<TwitterResultComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TwitterResultComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TwitterResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
