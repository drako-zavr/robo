import { api } from 'boot/axios';
import { Teacher } from '../types/index';

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
