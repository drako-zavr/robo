import { api } from 'boot/axios';
import { Package } from '../models/package';

export function usePackages() {
    const fetchPackages = async () => {
        try {
            const { data } = await api.get<Package[]>('/packages/list');
            return data;
        } catch (error) {
            console.error(error);
        }
        return [];
    };
    return {
        fetchPackages
    };
}
