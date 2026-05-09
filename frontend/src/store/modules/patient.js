const state = {
  patients: []
}

const mutations = {
  setPatients(state, patients) {
    state.patients = patients
  }
}

const actions = {
  async fetchPatients({ commit }) {
    const res = await fetch('/api/patients')
    const data = await res.json()
    commit('setPatients', data)
  }
}

const getters = {
  allPatients: (state) => state.patients
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
