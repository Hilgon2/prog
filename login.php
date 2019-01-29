    <div class="sufee-login d-flex align-content-center flex-wrap">
        <div class="container">
            <div class="login-content">
                <div class="login-logo">
                    <a href="index.html">
                        <img class="align-content" src="../images/logo.png" alt="">
                    </a>
                </div>
                <?php
                    if(isset($_SESSION['message']['login']) && !empty($_SESSION['message']['login'])) {
                        echo $_SESSION['message']['login'];
                        unset($_SESSION['message']['login']);
                    }
                ?>
                <div class="login-form">
                    <form method="post" action="">
                        <div class="form-group">
                            <label>Emailadres</label>
                            <input type="email" class="form-control" placeholder="Email" name="email">
                        </div>
                        <div class="form-group">
                            <label>Wachtwoord</label>
                            <input type="password" class="form-control" placeholder="Password" name="password">
                        </div>
                        <input type="submit" class="btn btn-success btn-flat m-b-30 m-t-30" name="login" value="Inloggen">
                        <div class="register-link m-t-15 text-center">
                            <p>Nog geen account? <a href="?page=register"> Registreren</a></p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>


    <script src="../assets/js/vendor/jquery-2.1.4.min.js"></script>
    <script src="../assets/js/popper.min.js"></script>
    <script src="../assets/js/plugins.js"></script>
    <script src="../assets/js/main.js"></script>


</body>
</html>
