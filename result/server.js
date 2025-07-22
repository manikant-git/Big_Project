var express = require('express'),
    app = express(),
    Redis = require('ioredis'),
    redis = new Redis({ host: 'redis', port: 6379, db: 0 });

app.set('view engine', 'pug');
app.set('views', './views');

const PARTIES = ['YSRCP', 'TDP', 'BJP', 'BRS', 'CONGRESS'];

app.get('/', async function(req, res) {
  try {
    let votes = {};
    for (let party of PARTIES) {
      votes[party] = parseInt(await redis.get(party)) || 0;
    }
    res.render('index', { votes: votes });
  } catch (e) {
    res.status(500).send('Error fetching votes!');
  }
});

app.listen(80, function () {
  console.log('Result app listening on port 80.');
});

