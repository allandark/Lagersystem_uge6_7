
export const getToken = (): string | null => {
  return localStorage.getItem("token");
};

export const setToken = (token: string) => {
  console.log("token set");
  localStorage.setItem("token", token);
};

export const clearToken = () => {
  localStorage.removeItem("token");
};
