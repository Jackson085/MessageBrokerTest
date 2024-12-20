import { Component } from '@angular/core';
import { VersionComponent } from './version/version.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'root';
}

// Die VersionComponent wird hier importiert und kann in der AppComponent verwendet werden
