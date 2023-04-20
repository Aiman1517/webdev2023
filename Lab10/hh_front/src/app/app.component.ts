import {Component, OnInit} from '@angular/core';
import {Vacancy} from "./models";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
  title = 'hh-front';

  companies: Vacancy[] = [];

  constructor() {
  }


}
