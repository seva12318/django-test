import { defineStore } from 'pinia'

export const useLessonsStore = defineStore({
    "id": "lessons",
    state: ()=>({
        students:[]
    }),
    actions: {
        async fetchStudents() {
            let r = await fetch("/api/students/");
            this.students = await r.json();
           
        },
        async deleteStudent(studentId) {
            let r = await fetch(`/api/students/${studentId}/`,{
                method: "DELETE"
            });
            await this.fetchStudents();
        },
        async addStudent(surname, name, patr, school) {
            let r = await fetch(`/api/students/`,{
                method: "POST",
                headers: {
                    "content-type":"application/json"
                },
                body: JSON.stringify({
                    surname,
                    name,
                    patr,
                    school
                })
            });
            await this.fetchStudents();
        },
        async updStudent(studentId, surname, name) {
            let r = await fetch(`/api/students/${studentId}/`,{
                method: "PATCH",
                headers: {
                    "content-type":"application/json"
                },
                body: JSON.stringify({
                    surname,
                    name
                })
            });
            await this.fetchStudents();
        }
    }
}) 