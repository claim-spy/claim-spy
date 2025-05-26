import {defineStore} from "pinia";
import {ref} from "vue";

export const useUserStore = defineStore('user', () => {
    const nom = ref('Nom test')
    const prenom = ref('Prenom test')

    function userToString() {
        return `${nom.value} ${prenom.value}`
    }

    return { userToString, nom, prenom }
})