class LoginService {

    constructor() {
        this.user = [
            { userId: 1, username: "user1", name: "User 1", password: "password", role:"admin"}
        ];
    }

    loginUser (obj) {
        if (obj['username'] === this.user[0].username && obj['password'] === this.user[0].password){
            return this.user;
        }
        return null;
    }

}

export default LoginService;
