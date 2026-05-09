import { createStore } from 'vuex'
import patient from './modules/patient'

export default createStore({
  modules: {
    patient
  }
})