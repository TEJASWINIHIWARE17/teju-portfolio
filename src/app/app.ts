import { Component } from '@angular/core';

import { About } from './about/about';
import { Skills } from './skills/skills';
import { Projects } from './projects/projects';
import { Experience } from './experience/experience';
import { Contact } from './contact/contact';
import { Navbar } from './navbar/navbar';

@Component({
  selector: 'app-root',

  imports: [
    About,
    Skills,
    Projects,
    Experience,
    Contact,
    Navbar
  ],

  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {

}