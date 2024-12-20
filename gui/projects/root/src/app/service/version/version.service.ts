import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VersionService {

  constructor(private http: HttpClient) { }

  getVersion(): Observable<VersionDto> {
    return this.http.get<VersionDto>("/version");
  }
}

export class VersionDto {
  major: number = 0;
  minor: number = 0;
  patch: number = 0;
}
