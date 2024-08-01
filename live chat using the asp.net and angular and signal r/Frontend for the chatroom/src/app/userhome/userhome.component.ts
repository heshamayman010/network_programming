import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ChatserviceService } from '../../services/chatservice.service';

@Component({
  selector: 'app-userhome',
  templateUrl: './userhome.component.html',
  styleUrl: './userhome.component.css'
})
export class UserhomeComponent {
 userform: FormGroup = new FormGroup({});
  submitted = false;
  openchat=false;

  erormessages: string[] = [];
  // The FormBuilder service provides methods for creating FormGroup, FormControl, and FormArray instances.
  constructor(
    private formbuilder: FormBuilder,
    private service: ChatserviceService
  ) {}

  // we will use it only to intialize the form once the component has been created
  ngOnInit(): void {
    this.intializeForm();
  }

  intializeForm() {
    // here we will make the restrictions we want as provided in the api project
    this.userform = this.formbuilder.group({
      name: [
        '',
        [
          Validators.required,
          Validators.minLength(3),
          Validators.maxLength(20),
        ],
      ],
    });
  }

  submittform() {
    this.erormessages = []; // intialize the error each time

    this.submitted = true;
    if (this.userform.valid) {
      // we must make the service return
      this.service.registerUser(this.userform.value).subscribe({
        next: () => {

          // now we will get the user namae 
          this.service.myname=this.userform.get('name')?.value;
          this.openchat=true;
          this.userform.reset();
          this.submitted==false;
        },
        error: (error) => {
          console.error('Error registering user', error);
          this.erormessages.push(error.message || 'Unknown error');
        },
      });
    }
  }

  // it will only be used to change the status of the openchat to false so the the users chat will be back again 
  closechat(){

this.openchat=false;

  }
}
