import { Component } from '@angular/core';
import {Vacancy} from "../models";
import {VacanciesService} from "../services/vacancies.service";
import {ActivatedRoute} from "@angular/router";
import {CompaniesService} from "../services/companies.service";

@Component({
  selector: 'app-company-vacancies',
  templateUrl: './company-vacancies.component.html',
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent {
  vacancies: Vacancy[] = [];
  company_name: string = '';

  constructor(private vac_service: VacanciesService, private route: ActivatedRoute, private comp_service: CompaniesService) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(() => {
      const id = Number(this.route.snapshot.paramMap.get('id'));
      this.vac_service.get_company_vacancies(id).subscribe((vacs) =>
        this.vacancies = vacs
      );
      this.comp_service.get_company(id).subscribe((company) =>
        this.company_name = company.name
      )
    }
    )
  }
}
