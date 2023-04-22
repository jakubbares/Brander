const getFromStorage = (key: string) => {
    let val = null;
    
    if (typeof window !== 'undefined') {
        val = window.localStorage.getItem(key)
    }

    return val;
}

const saveToStorage = (key: string, value: string) => {
    if (typeof window !== 'undefined') {
        window.localStorage.setItem(key, value)
    }
}


export { getFromStorage, saveToStorage }