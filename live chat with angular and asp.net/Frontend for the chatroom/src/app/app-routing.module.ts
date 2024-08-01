import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import path from 'node:path';
import { HomeComponent } from './home/home.component';
import { UserhomeComponent } from './userhome/userhome.component';

const routes: Routes = [


  {path:'admin',component:HomeComponent},
  {path:'',component:UserhomeComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
