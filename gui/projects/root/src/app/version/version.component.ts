import { Component } from '@angular/core';
import { VersionDto, VersionService } from '../service/version/version.service';

@Component({
  selector: 'app-version',
  templateUrl: './version.component.html',
  styleUrls: ['./version.component.scss']
})

export class VersionComponent {
  version: VersionDto = new VersionDto();
  
  constructor(private versionService: VersionService) { }

  ngOnInit(): void {
    this.versionService.getVersion().subscribe(data => {
      this.version = data;
    });
  }
}

