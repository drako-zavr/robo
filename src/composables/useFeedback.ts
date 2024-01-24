import { api } from 'boot/axios';
// import { Feedback } from '../models/feedback';
// import { ref } from 'vue';

export async function useFeedback(name: string, email: string, phone:string) {
    // const name = ref<string>(feedback.name),
    //     email = ref<string>(feedback.email),
    //     phone = ref<string>(feedback.phone);
    await api
        .post('/feedback/create/', {
            name: name,
            email: email,
            phone: phone
        })
        .catch((e) => {
            console.error(e);
        });
}