import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-contact',
  imports: [
    FormsModule,
    NgIf
  ],
  templateUrl: './contact.html',
  styleUrl: './contact.scss'
})
export class Contact {

  name = '';
  email = '';
  subject = '';
  message = '';

  isSending = false;
  successMessage = '';
  errorMessage = '';

  constructor(private http: HttpClient) {}

  sendMessage() {

    console.log('BUTTON CLICKED');

    const data = {
      name: this.name,
      email: this.email,
      subject: this.subject,
      message: this.message
    };

    console.log('DATA:', data);

    this.isSending = true;

    this.http.post(
      'http://127.0.0.1:8000/api/contact',
      data
    ).subscribe({

      next: (response) => {

        console.log('API SUCCESS:', response);

        this.successMessage =
          'Message sent successfully!';

        this.errorMessage = '';

        this.name = '';
        this.email = '';
        this.subject = '';
        this.message = '';

        this.isSending = false;
      },

      error: (error) => {

        console.error('API ERROR:', error);

        this.errorMessage =
          'Message could not be sent.';

        this.successMessage = '';

        this.isSending = false;
      }

    });
  }
}