### How to send an email with attatchments in Mailgun PHP

```
require 'vendor/autoload.php';
use Mailgun\Mailgun;

function sendMail($params) {
    $from = isset($params['from']) ? $params['from'] : 'default@from.com';
    $mailParams = array();
    $attachments = array();
    $mailParams['from'] = $params['sender_name'] . " <$from>";
    $mailParams['to'] = $params['to'];

    #$m->setFrom($params['sender_name' ] . " <$from>");
    if (isset($params['attachment'])) {
        $attachments[] = array('filePath' => $params['attachment']['path'], 'filename' => $params['attachment']['name']);
    }

    if (isset($params['custom_attachment'])) {
        foreach ($params['custom_attachment'] as $key => $file) {
            $attachments[] = array('filePath' => $file['path'], 'filename' => $file['name']);
        }
    }

    if (isset($params['replyTo'])) {
        if (is_array($params['replyTo'])) {
            foreach ($params['replyTo'] as $key => $email) {
                $mailParams['h:Reply-To'][] = $email;
            }
        } else {
            $mailParams['h:Reply-To'] = $params['replyTo'];
        }
    }

    $mailParams['subject'] = $params['subject'];
    $isHtml = $params['message'] != strip_tags($params['message']);
    if ($isHtml) {
        $mailParams['html'] = $params['message'];
    } else {
        $mailParams['text'] = $params['message'];
    }

    if (!empty($attachments)) {
        $mailParams['attachment'] = $attachments;
    }

    $mg = Mailgun::create('api_key_here');
    $status = $mg->messages()->send('mail.collectiveproperties.net', $mailParams);
    return $status;
}// sending email

$params = array();
$params['to'] = 'frank@court.com';
$params['from'] = 'wilson@prison.com';
$params['sender_name'] = 'Frank Castle';
$params['subject'] = 'IM COMING FOR YA';
$params['message'] = 'One batch! Two batch! Penny & dime!';
$params['replyTo'] = 'matt@nelsonandmurdock.com';
$params['attachment'] = array('path' => 'test.jpg', 'name' => 'test.jpg');
sendMail($params);
```