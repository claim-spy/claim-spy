<script setup>
import {LogOut, User2, Music} from "lucide-vue-next"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarFooter,
  SidebarHeader,
  SidebarSeparator,
} from "@/components/ui/sidebar"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

import { useRouter } from "vue-router"
import SidebarMenuAction from "@/components/ui/sidebar/SidebarMenuAction.vue"
const router = useRouter()


// import { toast } from "vue-sonner";
// import { makeApiRequest, removeAuthStorage} from "@/utils"
// import { useUser } from '@/composables/useUser'
// const { user } = useUser()

// async function logout(){
//     const refresh_token = localStorage.getItem("refresh_token")
    
//     if(refresh_token){
//       try {
//           await makeApiRequest({endpoint:'users/logout/', body:{"refresh": refresh_token}, method:'POST', useAccessToken:false})
//           toast.success('Logged out', {description: "You have been logged out successfully."});
//       }
//       catch(error){
//           toast.error('Logout failed', {description:"There was an error while logging out. Redirecting to the login page..."});
//       }
//     }
//     removeAuthStorage()
//     router.push({name:'Login'})
// }

let items = [
  {
    title: "Placeholder",
    name: "Placeholder",
    icon: Music,
  }
]

</script>

<template>
  <Sidebar>
    <SidebarHeader>
      <p class="ml-1 text-2xl font-semibold">Claim spy</p>
    </SidebarHeader>
    <SidebarSeparator class="m-auto mb-2"/>
    <SidebarContent>
      <SidebarGroup>
        <SidebarGroupContent>
          <SidebarMenu>
              <SidebarMenuItem v-for="item in items" :key="item.title">
                <SidebarMenuButton class="h-10" asChild>
                    <RouterLink :to="{ name : item.name, params:item.params}">
                      <component class="min-w-5 min-h-5 mr-2" :is="item.icon" />
                      <span class="text-lg">{{item.title}}</span>
                    </RouterLink>
                </SidebarMenuButton>
              </SidebarMenuItem>
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    </SidebarContent>
    <SidebarFooter>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger class="w-[100%] h-0" asChild>
            <SidebarMenuAction>
                <SidebarMenuButton variant="outline"  class="h-10 border-1 shadow" asChild>
                  <div class=" w-[100%] p-0">
                    <component class="min-w-5 min-h-5 mr-2" :is="User2" />
                    <span class="text-lg">PLACEHOLDER USERNAME</span>
                  </div>
                </SidebarMenuButton>
            </SidebarMenuAction>
          </DropdownMenuTrigger>
          <DropdownMenuContent side="right" align="start">
            <DropdownMenuItem @click="logout">
              <component :is="LogOut" />
              <a >Logout</a>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarFooter>
  </Sidebar>
</template>
