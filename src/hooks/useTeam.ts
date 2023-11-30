import { api } from 'boot/axios';
import { Teacher } from '../types/index';


// const fetchTeam = (): Promise<Teacher[]> => {
//     return new Promise((resolve, reject) => {
//       api
//         .get<Teacher[]>('team/list/')
//         .then((response) => {
//           resolve(response.data);
//         })
//         .catch((error) => {
//           console.error(error);
//           reject(error);
//         });
//     });
//   };
export function useTeam() {
    const fetchTeam = async () => {
        try {
            const { data } = await api.get<Teacher[]>('/team/list');
            return data;
        } catch (error) {
            console.error(error);
        }
        return [];
    };
    return {
        fetchTeam
    };
}
