import { refreshUser } from '@/utils.js'
import { ref } from 'vue'
import { useRouter } from 'vue-router'


const user = ref(JSON.parse(sessionStorage.getItem('user')))

function setUser(newUser) {
  sessionStorage.setItem('user', JSON.stringify(newUser))
  user.value = newUser
}

export function useUser() {
    const _router = useRouter()
    if(user.value === null){
        refreshUser(_router)
    }

  return { user, setUser }
}