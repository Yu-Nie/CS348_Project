import urls from "./urls"

export const login = (credential) => {
    // const loginUrl = `/login?username=${credential.username}&password=${credential.password}`;
  
    return fetch(urls.login, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // credentials: "include",
    }).then((response) => {
      if (response.status < 200 || response.status >= 300) {
        throw Error("Fail to log in");
      }
    });
  };
  
  export const signup = (data) => {

  };
  
  export const getMenus = (restId) => {
    return fetch(`/restaurant/${restId}/menu`).then((response) => {
      if (response.status < 200 || response.status >= 300) {
        throw Error("Fail to get menus");
      }
  
      return response.json();
    });
  };
  
  export const getRestaurants = () => {
    return fetch(urls.restaurants, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }).then((response) => {
      if (response.status < 200 || response.status >= 300) {
        throw Error("Fail to get restaurants");
      }
      return response.json();
    });
  };
  
  export const getCart = () => {

  };
  
  export const checkout = () => {

  };
  
  export const addItemToCart = (itemId) => {

  };