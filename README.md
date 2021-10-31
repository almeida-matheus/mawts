<h1 align="center">MAWTS</h1>

<div align="center">
    <a href="#about">About</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#how-to-use">How to use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#installation">Installation</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#contributing">Contributing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#license">License</a>
</div>

## About

A command line tool to easily manage AWS credentials and automate tasks 

### `In progress`

### To Do

- [x] input credentials in db
- [x] hash credentials in db
- [ ] save and get credentials in backend keyring os
- [x] list profiles in config
- [ ] list who am i - mfa, keys, expire days, etc
- [ ] assume role
- [ ] export credentials in shell - default
- [ ] export credentials in credentials file
- [ ] rotate credentials
- [ ] SSO integration

## How to use
Enter **mawts** followed by the **profile name** locate in `~/.aws/config`

Example:
```
mawts admin-prd
```
For more options type `mawts --help`

Output:
```
 ————————————————————————————————————————————————————————————————————
│ CLI to easily manage AWS credentials and automate tasks            │
 ————————————————————————————————————————————————————————————————————
│ positional                                                         │
│ profile_name  │ AWS profile to use                                 │
 ————————————————————————————————————————————————————————————————————
│ optional                                                           │
│ -e, --export  │ Export temporary credentials in default file       │
│ -h, --help    │ Show this help message                             │
│ -l, --list    │ List all available profiles                        │
│ -p, --profile │ AWS profile to use                                 │
│ -r, --rotate  │ Rotate your credentials keys                       │
│ -v, --version │ Show mawts version                                 │
│ -w, --whoami  │ Show AWS user info                                 │
 ————————————————————————————————————————————————————————————————————
```

## Installation

#### 1. Install python and pip
```
sudo apt install python3 && python3-pip
```

#### 2. Clone git repository
```
git clone "https://github.com/almeida-matheus/mawts"
```

#### 3. Install requeriments
```
cd mawts/
pip install requeriments.txt
```

#### 4. Execute install.sh
```
chmod +x install.sh
./install.sh
```

## Contributing
1. Fork the project
2. Create your branch (`git checkout -b branch-name`)
3. Add your changes (`git add .`)
4. Commit your changes (`git commit -m 'add some feature'`)
5. Push to the branch (`git push origin branch-name`)
6. Open a pull request

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.