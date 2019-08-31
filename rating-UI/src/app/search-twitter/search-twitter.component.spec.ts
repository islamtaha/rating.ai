import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchTwitterComponent } from './search-twitter.component';

describe('SearchTwitterComponent', () => {
  let component: SearchTwitterComponent;
  let fixture: ComponentFixture<SearchTwitterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchTwitterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchTwitterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
