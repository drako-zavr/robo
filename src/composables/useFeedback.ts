import { api } from 'boot/axios';

export async function useFeedback(name: string, email: string, phone:string) {
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